from . import db
import datetime


class RevokedTokenModel(db.Model):
    __tablename__ = 'revoked_tokens'
    id_ = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(120))
    blacklisted_on = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti=jti).first()
        return bool(query)