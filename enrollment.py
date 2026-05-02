# Simple logic for our University App
def check_capacity(current_enrolled, max_capacity):
    if current_enrolled < max_capacity:
        return "Space Available"
    else:
        return "Course Full"

# THE BUG: This is what students will fix
MAX_CAPACITY = 0
