from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlunoForm, ProfessorForm
from .models import Aluno, Professor, Instrumento
from django.contrib import messages

# Função para criar um novo aluno
def criar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)  # Cria o formulario com os dados do POST
        if form.is_valid():
            form.save() 
            return redirect('lista_alunos')  # Se salvar redireciona para a pagina de lista de alunos (ainda não existe)
    else:
        form = AlunoForm()  # Se o metodo for GET mostra um forms vazio
    return render(request, 'criar_aluno.html', {'form': form})  # Renderiza a pagina com o formulario de cadastro

# Função para editar os dados de um aluno existente
def editar_aluno(request, matricula):
    aluno = get_object_or_404(Aluno, matricula=matricula)  # Busca o aluno pelo numero de matricula ou retorna erro 404 (precisa disso mesmo Elias ou é bom tirar??)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)  # Usa os dados recebidos pra atualizar o aluno
        if form.is_valid(): 
            form.save() 
            return redirect('lista_alunos')  # Se der bom volta pra pagina de alunos (a gente muda pra algo melhor depois)
    else:
        form = AlunoForm(instance=aluno)  # Aqui tem que ser get então se for post vai dar erro
    return render(request, 'editar_aluno.html', {'form': form, 'aluno': aluno})  # Renderiza a página com o formulario de edição

# Função para excluir um aluno
def excluir_aluno(request, matricula):
    aluno = get_object_or_404(Aluno, matricula=matricula)  # Busca o aluno pelo número de matrícula ou retorna erro 404
    aluno.delete()  # Exclui o aluno do banco de dados
    return redirect('lista_alunos')  # Redireciona para a página de lista de alunos

# Cadastro do professor
def cadastrar_professor(request):
    if request.method == "POST":
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Professor cadastrado com sucesso!") # Deu bom
            return redirect('lista_professores') # depois a gente muda acho que melhor deixar logo a tela inicial sei la
    else:
        form = ProfessorForm() # Deu ruim

    return render(request, 'cadastrar_professor.html', {'form': form})

def lista_professores(request):
    professores = Professor.objects.all()
    return render(request, 'lista_professores.html', {'professores': professores})
