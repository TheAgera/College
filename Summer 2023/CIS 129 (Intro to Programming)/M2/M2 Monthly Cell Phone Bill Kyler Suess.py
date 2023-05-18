# Declarations for each of the modules below
months = 36
device_insurance = 300
cost_per_minute = 0.1  # $0.1 per minute
cost_per_message = 0.01
premium_plan = 75
regular_plan = 50
cost_per_gigabyte = 1
cost_per_hotspot_gigabyte = 5
streaming_services = 30
no_streaming_plan = 0
taxes = 0.06

# Module 1 to calculate the total device price over the installment period
def calculate_installment(months):
    device_price = 1000
    monthly_installment = device_price / months
    return monthly_installment

# Module 2 to calculate the total device insurance prive over the installment period
def calculate_insurance(months):
    monthly_insurance = device_insurance / months
    return monthly_insurance

# Module 3 to calculate the total cost of minutes
def calculate_minutes(cost_per_minute):
    minutes = 60
    monthly_minutes = cost_per_minute * minutes
    return monthly_minutes

# Module 4 to calculate the total clost of messages
def calculate_messages(cost_per_message):
    messages = 120
    monthly_messages = cost_per_message * messages
    return monthly_messages

# Module 5 to see how many devices are on the plan
def calculate_number_of_devices():
    num_devices = int(input("How many devices are on the phone plan?: "))
    return num_devices

# Module 6 to calculate the cost of the plan, based on plan option and number of devices
def calculate_phone_plan(is_premium_member, num_devices):
    monthly_plan = premium_plan if is_premium_member else regular_plan
    monthly_plan *= num_devices
    return monthly_plan

# Module 7 to calculate the cost of data used over the month in gigabytes
def calculate_data(cost_per_gigabyte):
    gigabytes = 5
    monthly_data = cost_per_gigabyte * gigabytes
    return monthly_data

# Module 8 to calculate the cost of hotspot data used over the month in gigabytes
def calculate_hotspot_data(cost_per_hotspot_gigabyte):
    gigabytes_hotspot = 5
    monthly_hotspot = cost_per_hotspot_gigabyte * gigabytes_hotspot
    return monthly_hotspot

# Module 9 used to determine whether or not the user has opted in for streaming services
def calculate_streaming_services_cost(is_streaming_member):
    monthly_cost = streaming_services if is_streaming_member else no_streaming_plan
    return monthly_cost

# Module 10 used to generate the bill, along with the user prompts for the if/else statements
def generate_bill():
    # Calls each previous module to grab their values, along with the if/else statements
    monthly_installment = calculate_installment(months)
    monthly_insurance = calculate_insurance(months)
    monthly_minutes = calculate_minutes(cost_per_minute)
    monthly_messages = calculate_messages(cost_per_message)
    
    user_monthly_input = input("Is the user a premium member? (yes/no): ")
    is_premium_member = user_monthly_input.lower() == 'yes'
    
    num_devices = calculate_number_of_devices()
    monthly_plan = calculate_phone_plan(is_premium_member, num_devices)
    
    monthly_data = calculate_data(cost_per_gigabyte)
    monthly_hotspot = calculate_data(cost_per_hotspot_gigabyte)
    
    user_streaming_input = input("Is the user a streaming subscriber? (yes/no): ")
    is_streaming_member = user_streaming_input.lower() == 'yes'
    streaming_services_cost = calculate_streaming_services_cost(is_streaming_member)

    # Once our function has the values, it can do the math.
    total_monthly_bill = (
        monthly_installment +
        monthly_insurance +
        monthly_minutes +
        monthly_messages +
        monthly_plan +
        monthly_data +
        monthly_hotspot +
        streaming_services_cost
    )


    total_bill_before_tax = total_monthly_bill
    total_bill_after_tax = total_bill_before_tax * (1 + taxes)

    # This section is here so the user can get a detailed breakdown of their bill
    print("--- Monthly Costs ---")
    print(f"Device Installment: ${monthly_installment}")
    print(f"Device Insurance: ${monthly_insurance}")
    print(f"Minutes: ${monthly_minutes}")
    print(f"Messages: ${monthly_messages}")
    print(f"Phone Plan: ${monthly_plan}")
    print(f"Data: ${monthly_data}")
    print(f"Hotspot: ${monthly_hotspot}")
    print(f"Streaming Services: ${streaming_services_cost}")
    print("--------------------")
    print(f"Total Monthly Bill: ${total_monthly_bill}")
    print("--------------------")
    print(f"Total Bill (Before Tax): ${total_bill_before_tax}")
    print(f"Total Bill (After Tax): ${total_bill_after_tax}")

# Fuctions have to actually be called. If this was not in the program, nothing would happen
# as the generate bill function needs to be called. 
generate_bill()

