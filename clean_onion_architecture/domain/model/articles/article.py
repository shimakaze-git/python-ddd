# -*- coding: utf-8 -*-

class Article:

    """
    public ArticleId _id
    private string __title;
    private string __body;
    private UserId __auther;
    private bool __is_publish;
    """
    def __init__(
        self,
        id,
        title : str,
        body : str,
        auther,
    ):
        self._id = id
        self.__title = title
        self.__body = body
        self.__auther = auther

        self.__is_publish = None

    def get_id(self):
        return self._id

    def publish(self):
        self.__is_publish = True

    def un_publish(self):
        self.__is_publish = False

    def is_same_id(self, id):
        pass

    def is_same_article(self):
        pass

    def is_written_by(self):
        pass



#         public T Transform<T>(IArticleDataTransformer<T> transformer)
#         {
#             transformer.Id(Id.Value);
#             transformer.Title(title);
#             transformer.Body(body);
#             return transformer.Build();
#         }

# using Domain.Domain.Model.Users;

# namespace Domain.Domain.Model.Articles {
#     public class Article
#     {
#         private string title;
#         private string body;
#         private UserId auther;
#         private bool isPublish;

#         public Article(
#             ArticleId id,
#             string title,
#             string body,
#             UserId auther
#         )
#         {
#             Id = id;
#             this.title = title;
#             this.body = body;
#             this.auther = auther;
#         }

#         public ArticleId Id { get; }

#         public void Publish()
#         {
#             isPublish = true;
#         }

#         public void Unpublish()
#         {
#             isPublish = false;
#         }

#         public bool IsSameId(ArticleId id)
#         {
#             return Id.Equals(id);
#         }

#         public bool IsSameArticle(Article article)
#         {
#             if (ReferenceEquals(null, article))
#             {
#                 return false;
#             }

#             if (ReferenceEquals(this, article))
#             {
#                 return true;
#             }

#             if (Id.Equals(article.Id))
#             {
#                 return true;
#             }

#             return false;
#         }

#         public bool IsWrittenBy(UserId auther)
#         {
#             return this.auther.Equals(auther);
#         }

#         public T Transform<T>(IArticleDataTransformer<T> transformer)
#         {
#             transformer.Id(Id.Value);
#             transformer.Title(title);
#             transformer.Body(body);
#             return transformer.Build();
#         }
#     }
# }