from django.db import models


class Post(models.Model):

    autors = models.ManyToManyField("users.User", related_name="my_posts")
    likes = models.ManyToManyField("users.User", related_name="post_likes")
    comments = models.ManyToManyField("users.User", related_name="commnets",
                                   through='Comment', through_fields=('post', 'user'))
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image =models.ImageField(blank=True, upload_to="posts_image/%Y/%m/%d/")
    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return self.title

class Comment(models.Model):

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField("users.User", related_name="comment_likes")
    text = models.TextField()
    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"

    def __str__(self):
        return self.user.__str__()+" "+self.post.__str__()