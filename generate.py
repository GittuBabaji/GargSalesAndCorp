import os

base_dir = "C:/Users/Asus/OneDrive/Desktop/khatta/garg-store"
src_main_java = os.path.join(base_dir, "src/main/java/com/example/gargstore")
src_main_resources = os.path.join(base_dir, "src/main/resources")
templates_dir = os.path.join(src_main_resources, "templates")
static_dir = os.path.join(src_main_resources, "static/css")

for d in [
    os.path.join(src_main_java, "model"),
    os.path.join(src_main_java, "repository"),
    os.path.join(src_main_java, "service"),
    os.path.join(src_main_java, "controller"),
    templates_dir,
    static_dir
]:
    os.makedirs(d, exist_ok=True)

print("Directories created.")
