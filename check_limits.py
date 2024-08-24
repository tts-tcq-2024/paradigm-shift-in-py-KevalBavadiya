
def is_temperature_ok(temperature):
    if temperature < 0 or temperature > 45:
        print('Temperature is out of range!')
        return False
    return True

def is_soc_ok(soc):
    if soc < 20 or soc > 80:
        print('State of Charge is out of range!')
        return False
    return True

def is_charge_rate_ok(charge_rate):
    if charge_rate > 0.8:
        print('Charge rate is out of range!')
        return False
    return True

def battery_is_ok(temperature, soc, charge_rate):
    return is_temperature_ok(temperature) and is_soc_ok(soc) and is_charge_rate_ok(charge_rate)


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
