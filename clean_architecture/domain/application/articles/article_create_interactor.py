# -*- coding: utf-8 -*-
'''
Created on 2019/2/11
@author: shimakaze-git
'''
import os
import sys
import json

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.dirname(os.path.abspath(__file__))
            )
        )
    )
)


class ArticleCreateInteractor:

    # def __init__(self, article_repository : IArticleRepository):
    def __init__(self, article_repository):
        self.__article_repository = article_repository

    def handle(self, request):
        # auther_id = UserId(request.auther_id)
        id = self.__article_repository.generate_id()
        # article = Article(id, request.Title, request.Body)

# using Domain.Domain.Model.Articles;
# using Domain.Domain.Model.Users;
# using UseCase.Articles.Create;

# public class ArticleCreateInteractor : IArticleCreateUseCase
# {
#     private readonly IArticleRepository articleRepository;

#     public ArticleCreateInteractor(IArticleRepository articleRepository)
#     {
#         this.articleRepository = articleRepository;
#     }

#     public ArticleCreateResponse Handle(ArticleCreateRequest request)
#     {
#         var autherId = new UserId(request.AutherId);
#         var id = articleRepository.GenerateId();
#         var article = new Article(id, request.Title, request.Body, autherId);
#         articleRepository.Save(article);
#         return new ArticleCreateResponse(id.Value);
#     }
# }
