from django.shortcuts import render, get_object_or_404, redirect
from .models import Aluno
from .forms import AlunoForm
from  django.contrib.auth.decorators import login_required

def alunoView(request):
    alunos = Aluno.objects.all()
    return render(request, 'main/list.html', {'alunos':alunos}) 

def alunoIdView(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    return render(request, 'main/aluno.html', {'aluno':aluno})


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

def exemplo(request):

    if request.method == 'POST':
        name = request.POST.get('nome', None)
        email = request.POST.get('email', None)
        telefone = request.POST.get('telefone', None)
        
        print(name , email, telefone)
        #Aluno.objects.create(nome=name, email=email, telefone=telefone)
        
    
    return render(request, 'main/indexx.html')

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

def deleteAluno(request, id):
    aluno=get_object_or_404(Aluno,pk=id)
    aluno.delete()
    return redirect('/')