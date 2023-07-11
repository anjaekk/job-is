async def add_posting_views(db, post):
    post.views += 1
    db.commit()
    db.refresh(post)