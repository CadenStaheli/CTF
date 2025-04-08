from flask import Flask, make_response, render_template

app = Flask(__name__)

@app.route('/lev3l2.html')
def lev3l2():
    resp = make_response(render_template("lev3l2.html"))

    fake_cookies = {
        "sessionID": "12345",
        "tracking": "user_83928",
        "authToken": "fakeAuth765",
        "userPrefs": "dark_mode",
        "cartID": "cart_349023",
        "port": "#3 _the_flag}",
        "visitCount": "15",
        "lastLogin": "2025-04-03T10:20:30Z",
        "userRole": "guest",
        "device": "mobile",
        "support": "#2 _NOT",
        "connectionType": "wifi",
        "subscription": "free",
        "theme": "light",
        "securityLevel": "low",
        "notification": "enabled",
        "backupCode": "N3TF49L",
        "emailVerified": "true",
        "phoneVerified": "false",
        "holder": "#1 ctf{This_is",
        "apiKey": "FAKE-123-456",
        "lastPurchase": "None",
        "checkoutStatus": "pending",
        "betaTester": "false",
        "language": "en-US",
        "supportTicket": "open",
        "referralCode": "XYZ987",
        "promoUsed": "SUMMER2025",
        "featureFlag": "enabled",
        "siteVersion": "1.2.3",
        "experimentGroup": "A",
        "surveyCompleted": "false",
        "location": "hidden",
        "vpnStatus": "on",
        "advertisingID": "ad_40239",
        "captchaPassed": "true",
        "debugMode": "off"
    }
    
    for key, value in fake_cookies.items():
        resp.set_cookie(key, value, httponly=True, secure=True)

    return resp

if __name__ == '__main__':
    app.run(debug=True)
