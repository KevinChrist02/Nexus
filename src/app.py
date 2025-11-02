import psutil
from flask import Flask, render_template

app = Flask(__name__)


def get_system_stats():
    stats = {}

    # Number of logical CPUs in the system
    stats["cpu_count"] = psutil.cpu_count()

    # System-wide CPU utilization as a percentage
    stats["cpu_percent"] = psutil.cpu_percent(interval=1)

    # CPU frequency in Mhz
    stats["cpu_freq_current"] = (
        int(psutil.cpu_freq().current) if psutil.cpu_freq() else "N/A"
    )

    mem = psutil.virtual_memory()

    # Total physical memory (exclusive swap)
    stats["mem_total"] = round(mem.total / (1024**3), 2)

    # Memory used
    stats["mem_used"] = round(mem.used / (1024**3), 2)

    # The percentage usage calculated as (total - available) / total * 100
    stats["mem_percent"] = mem.percent

    # Disk partitions (for root /)
    disk = psutil.disk_usage("/")

    stats["disk_total"] = round(disk.total / (1024**3), 2)
    stats["disk_used"] = round(disk.used / (1024**3), 2)
    stats["disk_percent"] = disk.percent

    # Sensors
    stats["sensors_temperatures"] = psutil.sensors_temperatures()

    return stats


@app.route("/")
def dashboard():
    system_data = get_system_stats()
    return render_template("index.html", **system_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
