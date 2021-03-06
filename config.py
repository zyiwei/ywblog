import os
basedir=os.path.abspath(os.path.dirname(__file__))


class Config:
	SECRET_KEY=os.environ.get('SECRET_KEY') or 'hard to guess string'
	SQLALCHEMY_COMMIT_ON_TEARDOWN=True
	FLASKY_POSTS_PER_PAGE=10
	FLASKY_COMMENTS_PER_PAGE=10
	FLASKY_USERS_PER_PAGE=20
	FLASKY_MAIL_SUBJECT_PREFIX='[Flasky]'
	FLASKY_MAIL_SENDER=os.environ.get('FLASKY_MAIL_SENDER')
	FLASKY_ADMIN=os.environ.get('FLASKY_ADMIN')
	PRESERVE_CONTEXT_ON_EXCEPTION = False
	SQLALCHEMY_RECORD_QUERIES=True
	SQLALCHEMY_TRACK_MODIFICATIONS=True
	FLASKY_SLOW_DB_QUERY_TIME=0.5

	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG=True
	MAIL_SERVER='smtp.qq.com'
	MAIL_PORT=587
	MAIL_USE_TLS=True
	MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
	SQLALCHEMY_DATABASE_URI=os.environ.get('DEV_DATABSE_URL') or 'sqlite:///'+os.path.join(basedir,'data-dev.sqlite')

class TestingConfig(Config):
	TESTING=True
	SQLALCHEMY_DATABASE_URI=os.environ.get('TEST_DATABASE_URL') or 'sqlite:///'+os.path.join(basedir,'data-dev.sqlite')
	WTF_CSRF_ENABLED=False

class ProductionConfig(Config):
	SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or 'sqlite:///'+os.path.join(basedir,'data.sqlite')

config={
	'development':DevelopmentConfig,
	'testing':TestingConfig,
	'producting':ProductionConfig,
	'default':DevelopmentConfig
} 