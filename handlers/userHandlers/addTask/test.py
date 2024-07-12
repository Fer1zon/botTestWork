from datetime import datetime, timedelta




print()

if (datetime.now() - (datetime.now() + timedelta(hours=-1))).seconds < 0:
    print(1)

print((datetime.now() - (datetime.now() + timedelta(hours=1))).seconds)


