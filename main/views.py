from django.shortcuts import render, get_object_or_404, redirect
from .models import Aluno
from .forms import AlunoForm
from  django.contrib.auth.decorators import login_required

@login_required #define que o usuário esteja logado, para ter acesso às informações. deve-se colocar em todas as funções privadas.
def alunoView(request):
    alunos = Aluno.objects.all().filter(user=request.user) #vai dar erro ao entrar sem logar. só funciona após criar o app accounts. 
    return render(request, 'main/list.html', {'alunos':alunos})

@login_required
def alunoIdView(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    return render(request, 'main/aluno.html', {'aluno':aluno})


@login_required
def newAluno(request):
    if request.method == 'POST':
        form =AlunoForm(request.POST)
        if form.is_valid():
            aluno = form.save(commit=False)
            aluno.user = request.user
            aluno.save()
            return redirect('/')
    else:
        form = AlunoForm()
    return render(request, 'main/add_aluno.html', {'form':form})

@login_required
def exemplo(request):

    if request.method == 'POST':
        name = request.POST.get('nome', None)
        email = request.POST.get('email', None)
        telefone = request.POST.get('telefone', None)
        
        print(name , email, telefone)
        #Aluno.objects.create(nome=name, email=email, telefone=telefone)
        
    
    return render(request, 'main/indexx.html')

@login_required
def editAluno(request, id):
    aluno=get_object_or_404(Aluno,pk=id)
    form=AlunoForm(instance=aluno)

    if(request.method=='POST'):
        form=AlunoForm(request.POST, instance=aluno)

        if(form.is_valid()):
            aluno.save()
            return redirect('/')
        else:
            return render(request, 'main/edit_aluno.html', {'form':form,'aluno':aluno})
    else:
        return render(request, 'main/edit_aluno.html',{'form':form,'aluno':aluno})

@login_required
def deleteAluno(request, id):
    aluno=get_object_or_404(Aluno,pk=id)
    aluno.delete()
    return redirect('/')