from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mars_weather_data.db'
db = SQLAlchemy(app)

sol_args = reqparse.RequestParser()
sol_args.add_argument("temperature", type=float, required=False)
sol_args.add_argument("pressure", type=float, required=False)
sol_args.add_argument("horizontal_wind_speed", required=False)
sol_args.add_argument("season", type=str, required=False)

resource_fields = {
    'id': fields.Integer,
    'temperature': fields.Float,
    'pressure': fields.Float,
    'horizontal_wind_speed': fields.Float,
    'season': fields.String,
}


class MarsData(Resource):
    @marshal_with(resource_fields)
    def get(self, sol_id):
        result = SolModel.query.filter_by(id=sol_id).first()
        if not result:
            abort(404, message="Sol_id does not exist...")
        return result

    @marshal_with(resource_fields)
    def put(self, sol_id):
        args = sol_args.parse_args()
        result = SolModel.query.filter_by(id=sol_id).first()
        if result:
            abort(409, message="Sol data already exists...")
        sol = SolModel(id=sol_id,
                       temperature=args['temperature'],
                       pressure=args['pressure'],
                       horizontal_wind_speed=args['horizontal_wind_speed'],
                       season=args['season']
                       )

        db.session.add(sol)
        db.session.commit()
        return sol, 201

    @marshal_with(resource_fields)
    def delete(self, sol_id):
        result = SolModel.query.filter_by(id=sol_id).first()
        db.session.delete(result)
        db.session.commit()
        return ''


api.add_resource(MarsData, "/mars_weather_data/<int:sol_id>")


class SolModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    temperature = db.Column(db.Float, nullable=True)
    pressure = db.Column(db.Float, nullable=True)
    horizontal_wind_speed = db.Column(db.Float, nullable=True)
    season = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f"Sol: {id}"


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
