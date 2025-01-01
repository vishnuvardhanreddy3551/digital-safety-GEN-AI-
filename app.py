from flask import Flask, render_template

app = Flask(__name__)

# Data for Digital Safety
concerns = [
    "Data Privacy: Your personal information could be stolen or misused.",
    "Identity Theft: Fraudsters may steal your identity for malicious purposes.",
    "Phishing: Fraudulent attempts to obtain sensitive information.",
    "Malware and Viruses: Harmful software can damage your device or steal information.",
    "Cyberbullying: Online harassment can harm individuals mentally and emotionally.",
    "Weak Passwords: Using easily guessable passwords can compromise your accounts.",
    "Public Wi-Fi Risks: Using unsecured public Wi-Fi for sensitive activities."
]

safety_tips = [
    "Use strong and unique passwords for each account.",
    "Enable two-factor authentication (2FA) wherever possible.",
    "Be cautious when clicking on links in emails, especially from unknown senders.",
    "Use a reliable antivirus program and keep it updated.",
    "Avoid sharing personal information on social media.",
    "Regularly update your software and operating systems.",
    "Be mindful of the data you share on public Wi-Fi networks."
]

digital_safety_guide = """
1. Always update your software and apps to patch security vulnerabilities.
2. Use multi-factor authentication (MFA) for an added layer of security.
3. Encrypt your sensitive data when storing it or sending it online.
4. Stay vigilant about phishing and scam emails; never share personal info.
5. Regularly backup important data to avoid data loss from cyber-attacks.
6. Monitor your financial transactions for suspicious activity.
7. Understand privacy policies and adjust settings accordingly on social media platforms.
"""

rules = [
    "Rule 1: Never share your password with anyone.",
    "Rule 2: Always check for HTTPS in the website URL before entering personal information.",
    "Rule 3: Do not download attachments from unknown emails.",
    "Rule 4: Avoid using public Wi-Fi for sensitive transactions like banking.",
    "Rule 5: Regularly change your passwords, especially for important accounts.",
    "Rule 6: Log out of your accounts when using shared or public computers."
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/concerns')
def show_concerns():
    return render_template('concerns.html', concerns=concerns)

@app.route('/tips')
def show_tips():
    return render_template('tips.html', tips=safety_tips)

@app.route('/guide')
def show_guide():
    return render_template('guide.html', guide=digital_safety_guide)

@app.route('/rules')
def show_rules():
    return render_template('rules.html', rules=rules)

if __name__ == "__main__":
    app.run(debug=True)
