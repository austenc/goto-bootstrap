import sublime, sublime_plugin, webbrowser

class GotoBootstrapCommand(sublime_plugin.WindowCommand):
	def run(self, page=''):
		# open a new page
		url = 'http://getbootstrap.com/'
		if(page != ''):
			url = url+page
		webbrowser.open_new_tab(url)
