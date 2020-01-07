from main.models import (
	CustomUser, Kudos
)

def get_user(pk):
	return CustomUser.objects.filter(pk=pk)

def get_all_users():
	return CustomUser.objects.all()

def get_kudos(pk):
	return Kudos.objects.filter(pk=pk)

def get_all_kudos_by_user(user_pk=None, user=None):
	if user_pk:
		user = CustomUser.objects.get(pk=user_pk)
		return Kudos.objects.filter(to_user=user)
	else:
		user = CustomUser.objects.get(pk=user.id)
		return Kudos.objects.filter(to_user=user)

def update_kudo_count(request):
	request.user.kudos_count = request.user.kudos_count - 1
	request.user.save()

def save_kudo(request):
	update_kudo_count(request)
	usr = CustomUser.objects.get(pk=request.data.get('to_user'))
	kudo = Kudos.objects.create(
		kudos_header=request.data.get('kudos_header'),
		kudos_message=request.data.get('kudos_message'),
		to_user=usr,
		from_user=request.user
	)
	return kudo.save()

def check_organization(request_user, to_sent_user):
	request_user = CustomUser.objects.get(pk=request_user)
	to_sent_user = CustomUser.objects.get(pk=to_sent_user)
	if str(request_user.orgranization.id) == str(to_sent_user.orgranization.id):
		return True

	return False

def reset_kudos_count_for_all_users():
	queryset = CustomUser.objects.all()
	queryset.update(kudos_count = 3)