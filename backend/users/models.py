from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CheckConstraint, Q, UniqueConstraint


class User(AbstractUser):
    email = models.EmailField(
        'Почта',
        max_length=150,
        unique=True
    )
    username = models.CharField(
        'Имя пользователя',
        blank=False,
        max_length=150,
        unique=True
    )
    first_name = models.CharField(
        'Имя',
        blank=False,
        max_length=150
    )
    last_name = models.CharField(
        'Фамилия',
        blank=False,
        max_length=150
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Пользователь-подписчик'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Пользователь (на кого подписаны)'
    )

    class Meta:
        constraints = (
            UniqueConstraint(
                fields=('user', 'following'),
                name='unique_following'
            ),
            CheckConstraint(
                check=~Q(user=models.F('following')),
                name='user_is_not_following',
            ),
        )

        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
