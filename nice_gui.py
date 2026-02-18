from nicegui import ui, app

# Simple credentials check
def try_login():
    if username.value == 'admin' and password.value == 'admin':
        ui.notify('Login Successful!', color='positive', icon='done')
        # Redirect or update UI here
    else:
        ui.notify('Invalid username or password', color='negative', icon='error')

# --- UI Design ---
# Use a background gradient and center the content
ui.query('body').classes('bg-gradient-to-br from-blue-50 to-indigo-100')

with ui.card().classes('absolute-center w-80 p-8 shadow-2xl rounded-xl border border-white'):
    # Header with icon
    with ui.column().classes('w-full items-center mb-4'):
        ui.icon('account_circle', size='70px').classes('text-indigo-600')
        ui.label('Welcome Back').classes('text-2xl font-bold text-gray-800')
        ui.label('Login to your account').classes('text-sm text-gray-500')

    # Input Fields
    username = ui.input('Username').classes('w-full mt-2').props('outlined dense')
    password = ui.input('Password', password=True, password_toggle_button=True)\
        .classes('w-full mt-4').props('outlined dense').on('keydown.enter', try_login)

    # Login Button
    ui.button('LOGIN', on_click=try_login)\
        .classes('w-full mt-6 bg-indigo-600 text-white rounded-lg h-12 font-bold hover:bg-indigo-700 transition-all')

    # Footer link
    ui.link('Forgot Password?', '#').classes('text-xs text-indigo-500 mt-4 self-center no-underline hover:underline')

# Add a floating dark mode switch for extra "modern" feel
ui.button(icon='dark_mode', on_click=lambda: ui.dark_mode().toggle())\
    .props('round flat').classes('absolute bottom-4 right-4')

ui.run(title='Admin Login')
