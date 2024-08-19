from django.shortcuts import render
from ATM.forms import WithdrawalForm, AccountForm
from django.shortcuts import render, get_object_or_404, redirect

from ATM.models import account, user


def index(request):
    bank_account = account.objects.all()
    clerk = user.objects.all()

    return render(request, 'index.html', {'bank_account': bank_account, 'clerk': clerk})



## *** Start withdraw functions ***
def calculate_notes(amount):
    notes = {10000: 0, 5000: 0, 2000: 0}

    # Priority on 10,000 bills
    if amount >= 10000:
        notes[10000] = amount // 10000
        amount %= 10000

    # Priority on 5,000 bills
    if amount >= 5000:
        notes[5000] = amount // 5000
        amount %= 5000

    # Finally 2,000 bills
    if amount >= 2000:
        notes[2000] = amount // 2000
        amount %= 2000

    # If a residue remains, the transaction fails
    if amount != 0:
        return None

    return notes


def generate_message(notes):
    message_parts = []

    for denomination, count in notes.items():
        if count > 0:
            message_parts.append(f"{count} billete{'s' if count > 1 else ''} de {denomination:,} colones")

    return f"Su dinero es " + ", ".join(message_parts)


def withdraw(request):
    if request.method == 'POST':
        form = WithdrawalForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            notes = calculate_notes(amount)

            if notes:
                message = generate_message(notes)
                return render(request, 'result.html', {'notes': notes, 'message': message})
            else:
                return render(request, 'result.html',
                              {'error': 'La transacción falló. No se puede entregar el monto exacto.'})
    else:
        form = WithdrawalForm()

    return render(request, 'withdraw.html', {'form': form})

## *** End withdraw functions ***


# Create (Crear)
def account_create(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account_list')
    else:
        form = AccountForm()
    return render(request, 'crud_accounts/account_form.html', {'form': form})

# Read (Leer)
def account_list(request):
    accounts = account.objects.all()
    return render(request, 'crud_accounts/account_list.html', {'accounts': accounts})

# Update (Actualizar)
def account_update(request, pk):
    acc = get_object_or_404(account, pk=pk)
    if request.method == "POST":
        form = AccountForm(request.POST, instance=acc)
        if form.is_valid():
            form.save()
            return redirect('account_list')
    else:
        form = AccountForm(instance=acc)
    return render(request, 'crud_accounts/account_form.html', {'form': form})

# Delete (Eliminar)
def account_delete(request, pk):
    acc = get_object_or_404(account, pk=pk)
    if request.method == "POST":
        acc.delete()
        return redirect('account_list')
    return render(request, 'crud_accounts/account_confirm_delete.html', {'account': account})


