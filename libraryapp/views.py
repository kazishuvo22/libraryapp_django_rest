from django.shortcuts import get_object_or_404
from django.utils.dateparse import parse_date
from knox.serializers import UserSerializer, User
from rest_framework import status, serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from libraryapp.models import Author, Book
from libraryapp.serializer import AuthorSerializer, BookSerializer


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_author(request):
    author = AuthorSerializer(data=request.data)

    # validating for already existing data
    if Author.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if author.is_valid():
        author.save()
        return Response(author.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_authors(request):
    # checking for the parameters from the URL
    if request.query_params:
        authors = Author.objects.filter(**request.query_params.dict())
    else:
        authors = Author.objects.all()

    # if there is something in items else raise error
    if authors:
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_author(request, pk):
    author = Author.objects.get(pk=pk)
    data = AuthorSerializer(instance=author, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_author(request, pk):
    author = get_object_or_404(Author, pk=pk)
    author.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_book(request):
    book = BookSerializer(data=request.data)

    # validating for already existing data
    if Book.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if book.is_valid():
        book.save()
        return Response(book.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_books(request):
    # checking for the parameters from the URL
    if request.query_params:
        books = Book.objects.filter(**request.query_params.dict())
    else:
        books = Book.objects.all()

    # if there is something in items else raise error
    if books:
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_book(request, pk):
    books = Book.objects.get(pk=pk)
    data = BookSerializer(instance=books, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def book_by_author_name(request):
    author_name = request.query_params.get('author_name', None)

    if author_name:
        authors = Author.objects.filter(author_name=author_name)

        if authors.exists():
            booklist = Book.objects.filter(author__in=authors)
            serializer = BookSerializer(booklist, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "No authors found with that name."}, status=status.HTTP_404_NOT_FOUND)

    return Response({"error": "Author name not provided."}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def book_by_published_date(request):
    start_date_str = request.query_params.get('start_date', None)
    end_date_str = request.query_params.get('end_date', None)

    if start_date_str and end_date_str:
        start_date = parse_date(start_date_str)
        end_date = parse_date(end_date_str)

        if start_date and end_date:
            books = Book.objects.filter(published_date__range=(start_date, end_date))
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Date format must be YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

    return Response({"error": "start_date and end_date are required."}, status=status.HTTP_400_BAD_REQUEST)
