import random

THINKING_MESSAGES = [
    "Balancing ledger dimensions…",
    "Herding tax forms…",
    "Summoning HR spirits…",
    "Generating fiscal enthusiasm…",
    "Consulting the payroll oracle…",
    "Sanitizing timecards…",
    "Decrypting compensation ley lines…",
    "Recalibrating net-to-gross vectors…",
    "Adjusting direct deposit gravity…",
    "Untangling W-2 wormholes…",
    "Training AI to understand PTO drama…",
    "Refactoring salary harmonics…",
    "Calibrating paycheck printers…",
    "Assembling interdimensional spreadsheets…",
    "Recharging onboarding matrix…",
    "Negotiating with payroll demons…",
    "Simulating annual review awkwardness…",
    "Neutralizing withheld emotions (and taxes)…",
    "Boosting morale subroutines…",
    "Stabilizing gross-to-net flux…",
    "Holographing HR compliance posters…",
    "Reconstructing payroll from ancient logs…",
    "Synchronizing benefit algorithms…",
    "Debugging overtime paradoxes…",
    "Compiling vacation calculations…",
    "Optimizing bonus distributions…",
    "Virtualizing employee happiness…",
    "Encrypting salary secrets…",
    "Defragmenting timesheet data…",
    "Initializing cyberbrain protocols…"
]

def get_thinking_message():
    """Return a random thinking message from the predefined list."""
    return random.choice(THINKING_MESSAGES)

spinner_css = """
<style>
  /* Animated cyber brain spinner */
  [data-testid="stSpinner"] {
    position: fixed !important;
    top: 50% !important;
    left: 50% !important;
    transform: translate(-50%, -50%) !important;
    z-index: 9999 !important;
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
    width: 300px !important;
    height: 200px !important;
  }
  
  [data-testid="stSpinner"]::before {
    content: '';
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    z-index: -1;
    backdrop-filter: blur(8px);
  }
  
  [data-testid="stSpinner"] svg {
    display: none !important;
  }
  
  /* Cyber brain container - clear positioning */
  [data-testid="stSpinner"] > div {
    position: relative !important;
    width: 300px !important;
    height: 200px !important;
    background: transparent !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
  }
  
  /* Create metallic cyber brain */
  [data-testid="stSpinner"] > div::before {
    content: '🧠';
    position: absolute;
    top: 25%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 80px;
    animation: cyberBrainPulse 2.5s ease-in-out infinite;
    filter: 
      drop-shadow(0 0 15px #00ffff) 
      drop-shadow(0 0 25px #0080ff) 
      drop-shadow(0 0 35px #4040ff)
      contrast(1.2)
      brightness(1.1)
      saturate(0.3);
    z-index: 1;
  }

  /* Metallic neural network grid */
  [data-testid="stSpinner"] > div::after {
    content: '';
    position: absolute;
    top: 10px;
    left: 50%;
    width: 220px;
    height: 220px;
    transform: translateX(-50%);
    border: 1px solid rgba(0, 255, 255, 0.3);
    border-radius: 50%;
    background: 
      radial-gradient(circle at 25% 25%, #00ffff 1px, transparent 2px),
      radial-gradient(circle at 75% 25%, #0080ff 1px, transparent 2px),
      radial-gradient(circle at 25% 75%, #4040ff 1px, transparent 2px),
      radial-gradient(circle at 75% 75%, #8080ff 1px, transparent 2px),
      radial-gradient(circle at 50% 15%, #00ffff 0.5px, transparent 1px),
      radial-gradient(circle at 50% 85%, #0080ff 0.5px, transparent 1px),
      radial-gradient(circle at 15% 50%, #4040ff 0.5px, transparent 1px),
      radial-gradient(circle at 85% 50%, #8080ff 0.5px, transparent 1px),
      linear-gradient(45deg, transparent 49%, rgba(0,255,255,0.1) 50%, transparent 51%),
      linear-gradient(-45deg, transparent 49%, rgba(0,128,255,0.1) 50%, transparent 51%);
    animation: neuralGrid 4s linear infinite;
    z-index: 0;
  }
  
  /* Cyber brain pulse animation - more metallic */
  @keyframes cyberBrainPulse {
    0%, 100% { 
      transform: translateX(-50%) scale(1);
      filter: 
        drop-shadow(0 0 15px #00ffff) 
        drop-shadow(0 0 25px #0080ff) 
        drop-shadow(0 0 35px #4040ff)
        contrast(1.2)
        brightness(1.1)
        saturate(0.3);
    }
    50% { 
      transform: translateX(-50%) scale(1.05);
      filter: 
        drop-shadow(0 0 25px #00ffff) 
        drop-shadow(0 0 40px #0080ff) 
        drop-shadow(0 0 60px #4040ff)
        drop-shadow(0 0 80px #8080ff)
        contrast(1.4)
        brightness(1.3)
        saturate(0.2);
    }
  }
  
  /* Neural grid animation */
  @keyframes neuralGrid {
    0% { 
      transform: translateX(-50%) rotate(0deg);
      opacity: 0.7;
    }
    50% {
      opacity: 1;
    }
    100% { 
      transform: translateX(-50%) rotate(360deg);
      opacity: 0.7;
    }
  }
  
  /* Thinking text positioned below brain */
  [data-testid="stSpinner"] > div {
    color: #00ffff !important;
    font-weight: bold !important;
    font-size: 18px !important;
    text-shadow: 0 0 10px rgba(0, 255, 255, 0.8), 0 0 20px rgba(0, 128, 255, 0.6);
    animation: cyberTextGlow 2.5s ease-in-out infinite alternate;
    font-family: 'Courier New', monospace !important;
    letter-spacing: 2px !important;
    text-align: center !important;
    padding-top: 120px !important;
    position: relative !important;
    z-index: 2 !important;
  }
  
  @keyframes cyberTextGlow {
    from { 
      text-shadow: 
        0 0 10px rgba(0, 255, 255, 0.8), 
        0 0 20px rgba(0, 128, 255, 0.6),
        0 0 30px rgba(64, 64, 255, 0.4);
      color: #00ffff !important;
    }
    to { 
      text-shadow: 
        0 0 20px rgba(0, 255, 255, 1), 
        0 0 30px rgba(0, 128, 255, 0.8),
        0 0 40px rgba(64, 64, 255, 0.6),
        0 0 50px rgba(128, 128, 255, 0.4);
      color: #80c0ff !important;
    }
  }
  
  /* Additional hologram effect */
  [data-testid="stSpinner"] {
    animation: hologramFlicker 5s ease-in-out infinite;
  }
  
  @keyframes hologramFlicker {
    0%, 100% { opacity: 1; }
    10% { opacity: 0.95; }
    20% { opacity: 1; }
    30% { opacity: 0.98; }
    40% { opacity: 1; }
    90% { opacity: 0.97; }
  }
  
  /* Keep existing bouncing text styles for chat messages */
  .bouncing-text {
    display: inline-block;
    background: linear-gradient(45deg, #53d4f7, #ff6b6b, #4ecdc4, #45b7d1);
    background-size: 400% 400%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: bounce 1.5s ease-in-out infinite, gradientText 3s ease infinite;
    font-weight: bold;
    font-size: 1.2em;
  }
  
  .bouncing-text:nth-child(odd) {
    animation-delay: 0.1s;
  }
  
  .bouncing-text:nth-child(even) {
    animation-delay: 0.2s;
  }
  
  @keyframes bounce {
    0%, 20%, 50%, 80%, 100% {
      transform: translateY(0);
    }
    40% {
      transform: translateY(-10px);
    }
    60% {
      transform: translateY(-5px);
    }
  }
  
  @keyframes gradientText {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
  }
  
  /* Pulsing dots animation */
  .thinking-dots {
    animation: pulse 1.5s infinite;
  }
  
  .thinking-dots::after {
    content: '⚡️💫✨';
    animation: sparkle 2s infinite;
  }
  
  @keyframes pulse {
    0% { opacity: 0.4; }
    50% { opacity: 1; }
    100% { opacity: 0.4; }
  }
  
  @keyframes sparkle {
    0%, 100% { opacity: 0.3; transform: scale(1); }
    50% { opacity: 1; transform: scale(1.2); }
  }

  .st-emotion-cache-1b4ojvx {
    width: 0;
    height: 0;
    border-width: 0;
}
</style>
"""