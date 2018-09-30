from django.utils.translation import ugettext as _
from django.db import models
from django.contrib.auth import models as auth_models

class UserManager(auth_models.BaseUserManager):

    def create_user(self, email,first_name,last_name,password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.first_name=first_name
        user.last_name=last_name
        user.save(using=self._db)
        return user

    def create_superuser(self, email,last_name,password):
        user = self.create_user(email,first_name,last_name, password=password)
        user.is_superuser = user.is_staff = True
        user.save(using=self._db)
        return user

class User(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(unique=True,verbose_name=_('Correo Electrónico'))
    first_name = models.CharField(max_length=30, blank=True,verbose_name=_('Nombre(s)'))
    last_name = models.CharField(max_length=30, blank=True,verbose_name=_('Apellidos(s)'))
    is_staff = models.BooleanField(default=False,verbose_name=_('Administrador'))
    is_active = models.BooleanField(default=True,verbose_name=_('Activo'))
    date_joined = models.DateTimeField(auto_now_add=True,verbose_name=_('Fecha de alta'))

    phone = models.IntegerField(default=1,verbose_name=_('Teléfono'))
    extension = models.IntegerField(default=1,verbose_name=_('Extensión'))
    photo = models.ImageField(upload_to='fotoUsuarios', null=True, blank=True,verbose_name=_('Foto de perfil'))
    area = models.ForeignKey('Area',on_delete=models.CASCADE,null=True,verbose_name=_('Área'))
    cargo = models.CharField(max_length=150,null=True,verbose_name=_('Cargo'))

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    #def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #    if db_field.name == "Area":
    #        if self.is_superuser :
    #            kwargs["queryset"] = Area.objects.filter(name__in=['God', 'Demi God'])
    #        else :
    #            kwargs["queryset"] = Area.objects.filter(name__in=['God', 'Demi God'])
    #    return super().formfield_for_foreignkey(db_field, request, **kwargs)

    class Meta:
        verbose_name = _('Usuario')
        verbose_name_plural = _('Usuarios')
        ordering = ('id', )

    def __unicode__(self):
        return u'{0} ({1})'.format(self.get_full_name(), self.email)

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return u'{0} {1}'.format(self.first_name, self.last_name)

class Area(models.Model):
    areas = (
    ('desarrolladorDelSitio','desarrolladorDelSitio'),
        ('Direccion General','Direccion General'),
          ('Dirección Academica','Dirección Academica'),
            ('Subdirección de Investigación','Subdirección de Investigación'),
              ('Coordinación de Intercambios','Coordinación de Intercambios'),
              ('Coordinación de Proyectos','Coordinación de Proyectos'),
            ('Subdirección de Docencia','Subdirección de Docencia'),
              ('Coordinación de Servicios Escolares','Coordinación de Servicios Escolares'),
              ('Posgrado en la CDMX','Posgrado en la CDMX'),
              ('Posgrado en LINGÜÍSTICA','Posgrado en LINGÜÍSTICA'),
              ('Posgrado en OCCIDENTE','Posgrado en OCCIDENTE'),
              ('Posgrado en SURESTE','Posgrado en SURESTE'),
              ('Posgrado en GOLFO','Posgrado en GOLFO'),
              ('Posgrado en PENINSULAR','Posgrado en PENINSULAR'),
              ('Posgrado en NORESTE','Posgrado en NORESTE'),
            ('Subdirección de Bibliotecas','Subdirección de Bibliotecas'),
            ('Subdirección de Difusión y Publicaciones','Subdirección de Difusión y Publicaciones'),
              ('Coordinación de Publicaciones','Coordinación de Publicaciones'),
              ('Coordinación de difusión','Coordinación de difusión'),
            ('Subdirección de Informática','Subdirección de Informática'),
              ('Coordinación de Sistemas','Coordinación de Sistemas'),
          ('Dirección de Vinculación','Dirección de Vinculación'),
          ('Dirección de Administración','Dirección de Administración'),
            ('Coordinación de Planeación y Control','Coordinación de Planeación y Control'),
            ('Unidad de Trasparencia','Unidad de Trasparencia'),
            ('Subdirección de Recursos Financieros','Subdirección de Recursos Financieros'),
              ('Jefatura de Presupuestos','Jefatura de Presupuestos'),
              ('Jefatura de Contabilidad','Jefatura de Contabilidad'),
              ('Jefatura de Recursos Humanos','Jefatura de Recursos Humanos'),
              ('Jefatura de Servicios Generales','Jefatura de Servicios Generales'),
              ('Jefatura de Recursos Materiales','Jefatura de Recursos Materiales'),
              ('Coordinación de Archivo','Coordinación de Archivo'),
              ('Coordinación de Admin Financiera de Proyectos','Coordinación de Admin Financiera de Proyectos'),
        ('Unidades Regionales','Unidades Regionales'),
          ('Dirección Regional Golfo','Dirección Regional Golfo'),
          ('Dirección Regional Pacifico Sur','Dirección Regional Pacifico Sur'),
          ('Dirección General Sureste','Dirección General Sureste'),
          ('Dirección General Occidente','Dirección General Occidente'),
          ('Dirección Regional Peninsular','Dirección Regional Peninsular'),
          ('Dirección Regional Noreste','Dirección Regional Noreste'),
            ('Jefatura de Administración','Jefatura de Administración'),
            ('Jefatura de Biblioteca','Jefatura de Biblioteca'),
    )
    tiposArea = (('Dirección','Dirección'),('Subdirección','Subdirección'),('Coordinación/Jefatura','Coordinación/Jefatura'),)

    nombre_area = models.CharField(max_length=150,choices=areas,unique=False,)
    subarea = models.ForeignKey('self',on_delete='CASCADE',blank=True,null=True)
    tipo_de_area = models.CharField(max_length=150,choices=tiposArea,default='Coordinación/Jefatura',)
    es_area_restringida = models.BooleanField(default=False)
    codigo_restriccion = models.CharField(max_length=15,blank=True,null=True)
    #asunto = models.ForeignKey('Asunto',on_delete='CASCADE',blank=True,null=True)
    clave_area = models.CharField(max_length=15,unique=True,)
    clave_area_num = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return self.nombre_area

    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas'
