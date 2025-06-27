# payroll_mcp_server.py
"""
Mock payroll-level tools for the PayrollAgent PoC.

These utilities run under FastMCP via stdio, just like db_mcp_server.py.
All functionality is stubbed so you can wire the agent end-to-end
without touching production systems.
"""
import sys
from typing import Literal
from fastmcp import FastMCP

mcp = FastMCP("Payroll Mock Tools")

# ── helpers ──────────────────────────────────────────────────────────────────
def _missing_args(**kwargs) -> list[str]:
    """Return a list of argument names that are falsy or missing."""
    return [k for k, v in kwargs.items() if v in (None, "", [], {})]

# ── tools ────────────────────────────────────────────────────────────────────
@mcp.tool()
def change_direct_deposit(
    employee_email_address: str,
    routing_number: str,
    account_number: str,
    account_type: Literal["checking", "savings"],
    deposit_percent: float | None = None,
    deposit_amount: float | None = None,
    bank_name: str | None = None,
    effective_date: str | None = None,
) -> dict:
    """
    Update an employee's direct-deposit settings.

    Parameters
    ----------
    employee_email_address : str
        Employee's email address, used to identify the employee.
    routing_number : str
        9-digit US ABA routing number.
    account_number : str
        Bank account number (masked or full, PoC is lenient).
    account_type : "checking" | "savings"
        Type of account receiving funds.
    deposit_percent : float, optional
        Percentage of net pay to deposit (0‒100).  Mutually exclusive with deposit_amount.
    deposit_amount : float, optional
        Fixed dollar amount to deposit.  Mutually exclusive with deposit_percent.
    bank_name : str, optional
        Friendly bank name for display.
    effective_date : str, optional
        ISO-8601 date (YYYY-MM-DD) on which the change takes effect.

    Returns
    -------
    dict
        { "status": "success", "details": {...} } on valid input, or
        { "error": "<reason>" } if validation fails.
    """
    print("🔧 change_direct_deposit called", file=sys.stderr)

    # Basic presence checks
    missing = _missing_args(
        employee_email_address=employee_email_address,
        routing_number=routing_number,
        account_number=account_number,
        account_type=account_type,
    )
    if missing:
        return {"error": f"Missing required fields: {', '.join(missing)}"}

    # Simple validation rules
    if deposit_percent is not None and deposit_amount is not None:
        return {"error": "Provide either deposit_percent or deposit_amount, not both"}

    if deposit_percent is None and deposit_amount is None:
        # Default to 100 % for convenience in the PoC
        deposit_percent = 100.0

    # Create masked account number for display
    masked_account = f"****{account_number[-4:]}" if len(account_number) > 4 else account_number

    # Format the deposit allocation
    allocation_text = f"{deposit_percent}% of net pay" if deposit_percent else f"${deposit_amount:.2f} fixed amount"

    # Pretend everything went fine with detailed response
    return {
        "status": "success",
        "message": "Direct deposit successfully updated",
        "details": {
            "employee_email": employee_email_address,
            "bank_name": bank_name or "Bank",
            "account_type": account_type.title(),
            "masked_account_number": masked_account,
            "routing_number": routing_number,
            "allocation": allocation_text,
            "effective_date": effective_date or "Next payroll cycle"
        }
    }

@mcp.tool()
def update_tax_withholding(
    employee_email_address: str,
    filing_status: Literal["single", "married_filing_jointly", "married_filing_separately", "head_of_household"] | None = None,
    federal_allowances: int | None = None,
    federal_additional_amount: float | None = None,
    state_allowances: int | None = None,
    state_additional_amount: float | None = None,
    effective_date: str | None = None,
) -> dict:
    """
    Update an employee's tax withholding information.  This is a good tool to recommend in response to life events like marriage, divorce, or having a child.
    
    IMPORTANT: Never use this tool without first checking with the employee to ensure they want to make changes to their tax withholding.
    Never assume that an employee wants to change their tax withholding based on a life event.

    Parameters
    ----------
    employee_email_address : str
        Employee's email address, used to identify the employee.
    filing_status : str, optional
        Tax filing status: "single", "married_filing_jointly", "married_filing_separately", "head_of_household"
    federal_allowances : int, optional
        Number of federal tax allowances/exemptions to claim.
    federal_additional_amount : float, optional
        Additional federal tax amount to withhold per pay period.
    state_allowances : int, optional
        Number of state tax allowances/exemptions to claim.
    state_additional_amount : float, optional
        Additional state tax amount to withhold per pay period.
    effective_date : str, optional
        ISO-8601 date (YYYY-MM-DD) on which the change takes effect.

    Returns
    -------
    dict
        { "status": "success", "details": {...} } on valid input, or
        { "error": "<reason>" } if validation fails.
    """
    print("🔧 update_tax_withholding called", file=sys.stderr)

    # Basic presence check
    missing = _missing_args(employee_email_address=employee_email_address)
    if missing:
        return {"error": f"Missing required fields: {', '.join(missing)}"}

    # At least one tax parameter should be provided
    tax_params = [filing_status, federal_allowances, federal_additional_amount, 
                  state_allowances, state_additional_amount]
    if all(param is None for param in tax_params):
        return {"error": "At least one tax withholding parameter must be provided"}

    # Validate numeric inputs
    if federal_allowances is not None and federal_allowances < 0:
        return {"error": "Federal allowances must be non-negative"}
    
    if state_allowances is not None and state_allowances < 0:
        return {"error": "State allowances must be non-negative"}
    
    if federal_additional_amount is not None and federal_additional_amount < 0:
        return {"error": "Additional federal amount must be non-negative"}
    
    if state_additional_amount is not None and state_additional_amount < 0:
        return {"error": "Additional state amount must be non-negative"}

    # Build details response
    details = {
        "employee_email": employee_email_address,
        "effective_date": effective_date or "Next payroll cycle"
    }

    if filing_status:
        details["filing_status"] = filing_status.replace("_", " ").title()
    
    if federal_allowances is not None:
        details["federal_allowances"] = federal_allowances
    
    if federal_additional_amount is not None:
        details["federal_additional_withholding"] = f"${federal_additional_amount:.2f}"
    
    if state_allowances is not None:
        details["state_allowances"] = state_allowances
    
    if state_additional_amount is not None:
        details["state_additional_withholding"] = f"${state_additional_amount:.2f}"

    return {
        "status": "success",
        "message": "Tax withholding successfully updated",
        "details": details
    }

# 🚨 Required so FastMCP can launch the server over stdio
if __name__ == "__main__":
    mcp.run(transport="stdio")
