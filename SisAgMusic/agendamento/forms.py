# Importações necessárias para os formulários
from django import forms
from .models import Aluno, Professor, InstrumentoEnum, Instrumento
from django.contrib.auth.models import User  # Importando o modelo User padrão do Django

# Formulario do Aluno
class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno  # Define que o formulario é baseado no modelo Aluno
        fields = ['nome', 'email', 'curso']  # Define os campos que serão exibidos no formulario



# Formulário do Professor
class ProfessorForm(forms.ModelForm):
    instrumentos = forms.MultipleChoiceField(  # Permite selecionar múltiplos instrumentos
        choices=InstrumentoEnum.choices(),  # Obtém as opções do InstrumentoEnum
        widget=forms.CheckboxSelectMultiple,  # Usa checkboxes para seleção
        label="Instrumentos (máximo de 3)"  # Rótulo para o campo
    )

    class Meta:
        model = Professor  # Define que o formulário é baseado no modelo Professor
        fields = ['nome', 'nascimento', 'cpf', 'rg', 'instrumentos']  # Campos a serem exibidos no formulário

    def clean_instrumentos(self):
        instrumentos = self.cleaned_data['instrumentos']  # Obtém os instrumentos selecionados
        if len(instrumentos) > 3:  # Verifica se foram selecionados mais de 3 instrumentos
            raise forms.ValidationError("Selecione no máximo 3 instrumentos.")  # Erro caso exceda o limite
        return ", ".join(instrumentos)  # Retorna os instrumentos como uma string separada por vírgulas

    def save(self, commit=True):
        # Cria um usuário para o professor com base nas informações fornecidas
        user = User.objects.create(
            first_name=self.cleaned_data['nome'],  # Nome do professor
            email=self.cleaned_data['cpf'],  # Usa o CPF como email para manter unicidade
            username=self.cleaned_data['cpf']  # O CPF é usado como o username
        )

        # Cria um objeto Professor com os dados fornecidos
        professor = Professor.objects.create(
            usuario=user,  # Relaciona o professor com o usuario criado
            nome=self.cleaned_data['nome'],  # Nome do professor
            nascimento=self.cleaned_data['nascimento'],  # Data de nascimento
            cpf=self.cleaned_data['cpf'],  # CPF do professor
            rg=self.cleaned_data['rg'],  # RG do professor
            instrumentos=self.cleaned_data['instrumentos']  # Armazena os instrumentos como string
        )

        if commit:
            professor.save()  # Salva o professor no banco de dados

        return professor  # Retorna o objeto Professor criado


    class InstrumentoForm(forms.ModelForm):
        class Meta:
            model = Instrumento  # Define que o formulario é baseado no modelo Instrumento
            fields = ['nome']  # Exibe apenas o campo nome do instrumento
