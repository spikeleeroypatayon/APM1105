#!/usr/bin/env python
# coding: utf-8

# How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a
# mile.

# In[2]:


miles = float(input("how many miles: "))

kilometer = miles * 1.61

print(kilometer , "kilometer")



kilometer = float(input("how many kilometer: "))

mile = kilometer * 0.621

print(mile, "mile")


# If  you  run  a  10  kilometer  race  in  42  minutes  42  seconds,  what  is  your  average
# pace  (time  per  mile  in  minutes  and  seconds)?  What  is  your  average  speed  in
# miles per hour?

# In[ ]:


distance = float(input(" the distance in miles: "))
minutes_time = int(input(" the time in minutes: "))
seconds_time = int(input(" the time in seconds: "))


final_time_seconds = minutes_time* 60 + seconds_time
pace_in_seconds = final_time_seconds / distance
pace_in_minutes = pace_in_seconds // 60
pace_in_seconds = int(pace_in_seconds % 60)
speed = distance / (final_time_seconds / 3600)


print(f"The pace is: {pace_in_minutes} minutes and {pace_in_seconds} seconds per mile")
print(f"The speed is: {speed:.2f} miles per hour")


# In[ ]:




