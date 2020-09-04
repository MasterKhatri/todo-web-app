from django import forms

class TodoListForm(forms.Form):
	text = forms.CharField(max_length = 45,
		widget = forms.TextInput(
			attrs = {'class': 'form-control transparent text-white mr-3', 'placeholder': 'E.g Do grocery shopping', 'aria-label': 'todo', 'aria-described-by': 'add-btn', 'id': 'exampleInputEmail1'}
			))