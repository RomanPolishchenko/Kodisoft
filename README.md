# Kodisoft
Kidisoft intership task. Data science

Description:
We create restaurants with interactive tables. There are a lot of different applications on the table. All applications are not placed in the menu. To increase profits, we need to know which small group of applications is best displayed on the table in a certain period of time and day of the week.

Task
Using revenue as a fundamental factor, which N applications should I show in the next ( hour/two hours/day) in the application menu? Create a tool that answers this question.
Input
We provide three datasets:
1. Applications:
• ApplicationName - application name
• StartTime - the time of starting the application
• EndTime - the time of closing the application
• ApplicationId – identificator of the unique application launching
2. Orders:
• Income – income from the order
• SessionId – identificator of the session when the order was made • Time – the time when the order was made
3. Links (For connection Applications and Orders):
• ApplicationId – identificator of the unique application launching
• SessionId – identificator of the session when the order was made • PlaceId – unique id of table place
• ApplicationName – application name
