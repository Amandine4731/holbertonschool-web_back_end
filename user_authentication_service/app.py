#!/usr/bin/env python3
"""
Flask APP
"""
from flask import Flask, jsonify, abort, request, redirect
from flask_cors import (CORS, cross_origin)
from auth import Auth
from sqlalchemy.orm.exc import NoResultFound


app = Flask(__name__)
AUTH = Auth()


@app.route("/")
def get_request() -> str:
    """ get request """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def register_user():
    """ register method """
    try:
        AUTH.register_user(request.form["email"], request.form["password"])
        return jsonify({"email": request.form['email'],
                        "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"})


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login():
    """ login """
    try:
        log = AUTH.valid_login(request.form["email"], request.form["password"])
        if log:
            user_sessionID = AUTH.create_session(request.form["email"])
            response = jsonify({"email": request.form["email"],
                                "message": "logged in"})
            response.set_cookie('session_id', user_sessionID)
            return response
        else:
            return abort(401)
    except ValueError:
        return abort(401)


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout():
    """ logout """
    session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect("/")
    return abort(403)


@app.route("/profile", methods=["GET"], strict_slashes=False)
def profile():
    """ get profile """
    cookie_session_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(cookie_session_id)
    if user:
        return jsonify({"email": user.email}), 200
    else:
        return abort(403)


@app.route("/reset_password", methods=["POST"], strict_slashes=False)
def reset_password():
    """ reset password """
    email = request.form["email"]
    try:
        token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": token}), 200
    except ValueError:
        return abort(403)


@app.route("/reset_password", methods=["PUT"], strict_slashes=False)
def update_password():
    """ update password """
    reset_token = request.form["reset_token"]
    email = request.form["email"]
    new_password = request.form["new_password"]
    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except ValueError:
        return abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
