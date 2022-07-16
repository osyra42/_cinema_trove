head = ""

def web_maker(root, category, title, episode):
    head = """f<!DOCTYPE html>
<html>
<head>
    <title>{episode}</title>
</head>    
"""
with open('ct_web/index.html', 'w') as f:
    f.write(head) 