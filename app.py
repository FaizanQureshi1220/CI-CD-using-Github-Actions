from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Single-File Flask App</title>
    <!-- Load Tailwind CSS from CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Apply the Inter font globally */
        body {
            font-family: 'Inter', sans-serif;
        }
    </style>
</head>
<body class="bg-gray-100 min-h-screen flex items-center justify-center p-4">

    <!-- Main Card Container -->
    <div class="bg-white p-8 md:p-12 rounded-xl shadow-2xl w-full max-w-lg text-center">
        
        <h1 class="text-4xl font-extrabold text-indigo-700 mb-4 tracking-tight">
            Hello from Flaskk! 
        </h1>
        
        <p class="text-xl text-gray-600 mb-8">
            This entire application is running from a single Python file.
        </p>

        <!-- Dynamic Content Example -->
        <div class="border-t border-gray-200 pt-6">
            <p class="text-sm font-medium text-gray-500 mb-2">
                Server Status:
            </p>
            <span id="status" class="inline-flex items-center px-4 py-1.5 rounded-full text-sm font-semibold tracking-wide transition duration-300
                                       bg-green-100 text-green-800 ring-2 ring-green-500 ring-opacity-50 hover:bg-green-200">
                🚀 Running Successfully!
            </span>
        </div>

        <p class="mt-8 text-xs text-gray-400">
            Powered by Python and a single route.
        </p>
    </div>

</body>
</html>
"""

@app.route('/')
def home():
    """
    Renders the HTML template string when the user accesses the root URL.
    """
    return render_template_string(HTML_TEMPLATE)


if __name__ == '__main__':
    print("Flask app running at http://127.0.0.1:5000/")
    app.run(debug=True)
