TEMPERATURE_LIMITS = (0, 45)
SOC_LIMITS = (20, 80)
CHARGE_RATE_LIMITS = (0, 0.8)
TOLERANCE_PERCENTAGE = 5  

class BatteryParameter:
    def __init__(self, name, value, limits, enable_warning=True):
        self.name = name
        self.value = value
        self.lower_limit, self.upper_limit = limits
        self.enable_warning = enable_warning
        self.warning_tolerance = (TOLERANCE_PERCENTAGE / 100) * self.upper_limit

    def is_within_limits(self):
        return self.lower_limit <= self.value <= self.upper_limit

    def get_warning_message(self):
        if not self.enable_warning:
            return ''
        
        if self.value <= self.lower_limit + self.warning_tolerance:
            return f'Warning: {self.name} approaching discharge!'
        
        if self.value >= self.upper_limit - self.warning_tolerance:
            return f'Warning: {self.name} approaching charge-peak!'
        
        return ''

    def is_ok(self):
        if not self.is_within_limits():
            if self.value < self.lower_limit:
                return False, f'{self.name} is too low!'
            return False, f'{self.name} is too high!'

        return True, self.get_warning_message()

class Battery:
    def __init__(self, temperature, soc, charge_rate):
        self.temperature = BatteryParameter("Temperature", temperature, TEMPERATURE_LIMITS)
        self.soc = BatteryParameter("State of Charge", soc, SOC_LIMITS)
        self.charge_rate = BatteryParameter("Charge Rate", charge_rate, CHARGE_RATE_LIMITS)

    def is_battery_ok(self):
        parameters = [self.temperature, self.soc, self.charge_rate]
        for parameter in parameters:
            is_ok, message = parameter.is_ok()
            if not is_ok:
                return False, message
            if message:  # In case of warning
                print(message)
        return True, "Battery is OK"

if __name__ == '__main__':
    assert(Battery(25, 70, 0.7).is_battery_ok()[0] is True)
    assert(Battery(50, 85, 0).is_battery_ok()[0] is False)
    assert(Battery(21, 78, 0.75).is_battery_ok()[0] is True)  
