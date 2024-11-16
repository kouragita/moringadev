def paginate(query, page, per_page):
    items = query.paginate(page, per_page, error_out=False)
    return {
        'items': items.items,
        'total': items.total,
        'page': items.page,
        'pages': items.pages,
    }