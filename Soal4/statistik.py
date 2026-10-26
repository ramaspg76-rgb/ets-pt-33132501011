def rentang(data):
    return (min(data), max(data))


def ringkasan(data):
    return {
        "jumlah": sum(data),
        "min": min(data),
        "maks": max(data),
        "rata": sum(data) / len(data),
    }


# --- Pemanggilan / uji ---
data = [12.0, 15.0, 15.0]

print("rentang  :", rentang(data))
r = ringkasan(data)
print("ringkasan:", r)
print("rata     :", r["rata"])