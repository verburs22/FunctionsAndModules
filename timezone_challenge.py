#sarah verburg 06-09

from datetime import datetime
import zoneinfo

# to make more efficient, combine code into a for loop
#video 324

#utc_now = datetime.now(timezone.utc)
local_now = datetime.now()
local_now = local_now.replace(microsecond=0)

#Paris
france_tz = zoneinfo.ZoneInfo('Europe/Paris')
france_now = local_now.astimezone(tz=france_tz)
print("Current time in Paris: \n", france_now, france_now.tzname())

#London
london_tz = zoneinfo.ZoneInfo('Europe/London')
london_now = local_now.astimezone(tz=london_tz)
print("Current time in London: \n", london_now, local_now.tzname())

#Hong Kong
hong_kong_tz = zoneinfo.ZoneInfo('Asia/Hong_Kong')
hong_kong_now = local_now.astimezone(tz=hong_kong_tz)
print("Current time in Hong Kong: \n", hong_kong_now, hong_kong_now.tzname())

#Nairobi
nairobi_tz = zoneinfo.ZoneInfo('Africa/Nairobi')
nairobi_now = local_now.astimezone(tz=nairobi_tz)
print("Current time in Nairobi: \n", nairobi_now, nairobi_now.tzname())
