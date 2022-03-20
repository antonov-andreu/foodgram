from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

COLOURS = (
    ('#9C9C9C', 'Серый'),
    ('#FFF68F', 'Желтый'),
    ('#00FF7F', 'Зеленый'),
    ('#FF6A6A', 'Красный'),
    ('#FF8247', 'Оранжевый'),
    ('#00F5FF', 'Синий'),
)
User = get_user_model()


class Ingredient(models.Model):
    name = models.CharField(
        'Название',
        max_length=200,
        null=False,
        blank=False
    )
    measurement_unit = models.CharField(
        'Мера измерения',
        max_length=200,
        null=False,
        blank=False
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Ингридиент'
        verbose_name_plural = 'Ингридиенты'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(
        'Название',
        max_length=200,
        unique=True,
        null=False,
        blank=False
    )
    color = models.CharField(
        'Цвет',
        max_length=7,
        unique=True,
        null=False,
        blank=False,
        choices=COLOURS,
    )
    slug = models.CharField(
        'Слаг',
        max_length=200,
        unique=True,
        null=False,
        blank=False
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(
        'Название',
        max_length=200,
        blank=False,
        null=False
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор'
    )
    text = models.TextField(
        'Описание',
        blank=False,
        null=False
    )
    tags = models.ManyToManyField(Tag, through='RecipeTags')
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredients'
    )
    cooking_time = models.PositiveIntegerField(
        'Время готовки',
        validators=[MinValueValidator(1)]
    )
    image = models.ImageField(
        'Фото рецепта',
        upload_to='recipes/',
        blank=False,
        null=False
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.name


class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.PROTECT,
        verbose_name='Ингридиент'
    )
    amount = models.PositiveIntegerField(
        'Количество',
        validators=[MinValueValidator(1)]
    )

    class Meta:
        verbose_name = 'Ингридиенты'
        verbose_name_plural = 'Ингридиенты'

    def __str__(self):
        return 'Ингридиент в рецепте'


class RecipeTags(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        verbose_name='Тег'
    )

    class Meta:
        verbose_name = 'Теги'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return 'Тег рецепта'


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorite',
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='in_favorite',
        verbose_name='Рецепт'
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'recipe'),
                name='unique_recipe_in_user_favorite'
            ),
        )
        ordering = ('-id',)
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'


class ShoppingList(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_list',
        verbose_name='Пользователь'
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name='Рецепт'
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'recipe'),
                name='unique_recipe_in_user_shopping_list'
            ),
        )
        ordering = ('-id',)
        verbose_name = 'Список покупок'
        verbose_name_plural = 'Списки покупок'
