from main.models import (
	CustomUser, Kudos
)

def get_user(pk):
	return CustomUser.objects.filter(pk=pk)

def get_all_users():
	return CustomUser.objects.all()

def get_kudos(pk):
	return Kudos.objects.filter(pk=pk)

def get_all_kudos_by_user(user_pk):
	user = CustomUser.objects.get(pk=user_pk)
	return Kudos.objects.filter(to_user=user)

def save_kudo(request):
	usr = CustomUser.objects.get(pk=request.data.get('to_user'))
	kudo = Kudos.objects.create(
		kudos_header=request.data.get('kudos_header'),
		kudos_message=request.data.get('kudos_message'),
		to_user=usr,
		from_user=request.user
	)
	return kudo.save()
