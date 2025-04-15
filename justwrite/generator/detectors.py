import os

def detect_style_files(static_dir):
    styles = []

    if not os.path.isdir(static_dir):
        print(f"{static_dir} is not a diectory")
        return styles
    
    for root,_ , files in os.walk(static_dir):
        for file in files:
            url_path = os.path.relpath(os.path.join(root, file), static_dir).replace('\\','/')

            if file.endswith('.css'):
                styles.append(url_path)

    return styles

def detect_script_files(static_dir):
    scripts = []

    if not os.path.isdir(static_dir):
        print(f"{static_dir} is not a directory")
        return scripts

    for root,_ , files in os.walk(static_dir):
        for file in files:
            url_path = os.path.relpath(os.path.join(root, file), static_dir).replace('\\', '/')
            
            if file.endswith('.js'):
                scripts.append(url_path)

    return scripts
