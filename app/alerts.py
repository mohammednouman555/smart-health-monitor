def generate_alerts(data):
    alerts = []

    if data.temperature > 100:
        alerts.append("High Temperature")

    if data.heart_rate is not None and (data.heart_rate < 60 or data.heart_rate > 100):
        alerts.append("Abnormal Heart Rate")

    if data.blood_pressure:
        try:
            systolic, diastolic = map(int, data.blood_pressure.split("/"))
            if systolic > 130 or diastolic > 90:
                alerts.append("High Blood Pressure")
        except:
            alerts.append("Invalid Blood Pressure Format")

    if data.water_ph < 6.5 or data.water_ph > 8.5:
        alerts.append("Unsafe Water pH")

    if data.water_tds > 150:
        alerts.append("High TDS")

    if data.water_turbidity > 1:
        alerts.append("High Turbidity")

    if data.contamination:
        alerts.append("Water Contamination Detected")

    return alerts