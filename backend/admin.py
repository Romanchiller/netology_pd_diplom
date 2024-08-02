from django.contrib import admin
from django.contrib.admin.exceptions import NotRegistered
from django.contrib.admin.options import InlineModelAdmin
from django.contrib.auth.admin import UserAdmin

from backend.models import User, Shop, Category, Product, ProductInfo, Parameter, ProductParameter, Order, OrderItem, \
    Contact, ConfirmEmailToken


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 2


class CategoryShopInline(admin.TabularInline):
    model = Category.shops.through
    extra = 1


class ProductInfoShopInline(admin.TabularInline):
    model = ProductInfo
    extra = 1


class ProductParameterInline(admin.TabularInline):
    model = ProductParameter
    extra = 1


class ParameterInfoInline(admin.TabularInline):
    model = ProductParameter


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


class ContactUserInline(InlineModelAdmin):
    model = Contact
    extra = 1


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Панель управления пользователями
    """
    model = User

    fieldsets = (
        (None, {'fields': ('email', 'password', 'type')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'company', 'position')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),

    )
    list_display = ('email', 'username', 'is_active', 'is_staff', 'company','type', 'shop',)

    list_filter = ['type', 'is_active', 'is_staff', 'company']








@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    model = Shop
    fieldsets = (
        (None, {'fields': ('name', 'state')}),
        ('Additional Info', {'fields': ('url', 'user')}),
    )
    list_display = ('name', 'user', 'url', 'state')
    inlines = [CategoryShopInline, ProductInfoShopInline]
    list_filter = ['state']
    readonly_fields = ['user']



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ['name',]
    exclude = ['shops']
    inlines = [CategoryShopInline]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['name', 'category',]
    list_filter = ['category']



@admin.register(ProductInfo)
class ProductInfoAdmin(admin.ModelAdmin):
    model = ProductInfo
    fieldsets = (
        (None, {'fields': ('product', 'model', ('external_id', 'quantity'))}),
        ('Цены', {'fields': ('price', 'price_rrc')}),
    )
    list_display = ('product', 'external_id', 'price', 'price_rrc', 'quantity')
    inlines = [ProductParameterInline]



@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    list_filter = []
    pass


@admin.register(ProductParameter)
class ProductParameterAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order
    fields = ('user', 'state')
    list_display = ('id', 'user', 'dt', 'state')
    inlines = [OrderItemInline, ]
    list_filter = ['state']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product_info', 'quantity']
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'city', 'phone')
    list_filter = ['city']




@admin.register(ConfirmEmailToken)
class ConfirmEmailTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'key', 'created_at',)
