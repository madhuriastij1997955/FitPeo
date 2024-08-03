def approve_vacation_requests(approved_requests, new_request):
    # Count the number of times each day has been granted
    day_count = {}

    for request in approved_requests:

        for day in request:
            day_count[day] = day_count.get(day, 0) + 1

    approved = []

    # Process the new vacation request
    for day in new_request:
        if day not in day_count or day_count[day] < 2:
            # Approve the request if the day hasn't been granted twice already
            approved.append(day)
            day_count[day] = day_count.get(day, 0) + 1

    return approved


approved_1 = [3, 6, 11, 15, 20, 23, 2, 28, 29]
request_1_1 = [9, 13, 17, 23, 25]

result = approve_vacation_requests(approved_1, request_1_1)
print(result)
