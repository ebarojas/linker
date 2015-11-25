from linkedin import linkedin

# Define CONSUMER_KEY, CONSUMER_SECRET,
# USER_TOKEN, and USER_SECRET from the credentials
# provided in your LinkedIn application

API_KEY = '78m7qhxi0ltzfe'
API_SECRET = 'uaSG9le3Iq01jkpf'
# API_KEY = '75ikzf7tubpe8b'
# API_SECRET = 'mG3ujuLsVfTEQukr'
RETURN_URL = 'http://localhost:8080/code'

authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL) #, linkedin.PERMISSIONS.enums.values())
print authentication.authorization_url  # open this url on your browser
# application = linkedin.LinkedInApplication(authentication)
# http://localhost:8080/code?code=AQQIclCouaVNogQppnZ0tuzaz8k-IN700xvJpbYvXK2IJWod-J5GqorX2qKZR4It6gV_UoH2yEYrTOuYnIknhslT74CwBMvbBjONGPFrcxKJAxZmKuw&state=1d6b1163f08aa0bb51e5d6697071559d
# https://localhost:8000/?code=AQRQglTv_nL6lGpYT1VuPKRVjgXoyMiibdDNYjzR_v9H9LM4EbdybziDgEbYfEJOOKOkq5vPU0G1g3WVN2djwS6pKnh5tjP6ky1aX_yraRqDpkS9C3g&state=fcb6805995568f449fb6eb4d7c358b22
application = linkedin.LinkedInApplication(token='AQX-FBbKwHxA2wBpLY_wvdHvoZrQK8TsWU6EaNgjh8yIhZB_XYym8HOQVC036sH8c2W9THCCB0gwXvT0uaOILD5OteN2DpcFzZBOo8ZDlDQKr6tAxhiUu2PqLvHWq4DiMbqjpYbgWsrjWciynDfsrLMu9dBeErg_Lf08IcGk5RKf1158FK0')

# authentication.authorization_code = 'AQSa3ZKTEZ79AT6eA0vwIksywcBI1fSqRcXEgzi2RWgdyl2UN0Hd0RAaNK_iOdhr4FKpQSdzRVcJePMP4fuwmb073rZmHPueZPcn4DCxfHGsEIPYtuY'
# print authentication.get_access_token()


# print application.get_profile(selectors=['id', 'first-name', 'last-name', 'location', 'distance', 'num-connections', 'skills', 'educations'])
print application.get_profile()

