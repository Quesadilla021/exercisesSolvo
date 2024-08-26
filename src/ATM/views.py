from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render
from djgentelella.settings import User

from ATM.forms import WithdrawalForm, AccountForm, AccountValidationForm
from django.shortcuts import render, get_object_or_404, redirect

from ATM.models import Account

@login_required
def inicio(request):
    bank_account = Account.objects.all()
    user = User.objects.all()

    return render(request, 'index.html', {'bank_account': bank_account, 'user': user})



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
            message_parts.append(f"{count} bill{'s' if count > 1 else ''} of {denomination:,} colones")

    return f"your money is " + ", ".join(message_parts)

@login_required
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
                              {'error': 'The transaction failed. The exact amount cannot be delivered.'})
    else:
        form = WithdrawalForm()

    return render(request, 'withdraws/withdraw.html', {'form': form})


@login_required
def validate_account(request):
    if request.method == 'POST':
        form = AccountValidationForm(request.POST, user=request.user)
        if form.is_valid():

            # Obtener la cuenta validada
            account_name = form.cleaned_data.get('account_name')
            pin_code = form.cleaned_data.get('pin_code')
            account = Account.objects.get(user=request.user, name=account_name, pin_code=pin_code)

            # Almacenar el ID de la cuenta en la sesión
            request.session['validated_account_id'] = account.id

            return redirect('withdraw')
    else:
        form = AccountValidationForm(user=request.user)

    return render(request, 'withdraws/insert_pin.html', {'form': form})


## *** End withdraw functions ***


# Create (Crear)
@permission_required('ATM.can_manage_client')
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
@permission_required('ATM.can_manage_client')
def account_list(request):
    accounts = Account.objects.all()
    return render(request, 'crud_accounts/account_list.html', {'accounts': accounts})

# Update (Actualizar)
def account_update(request, pk):
    acc = get_object_or_404(Account, pk=pk)
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
    acc = get_object_or_404(Account, pk=pk)
    if request.method == "POST":
        acc.delete()
        return redirect('account_list')
    return render(request, 'crud_accounts/account_confirm_delete.html', {'account': Account})


