
class CreateUpdateUserAdminMixin:
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.criado_por = request.user
        obj.atualizado_por = request.user
        return super().save_model(request, obj, form, change)

