class CalcentralUsersController < ApplicationController
  # GET /calcentral_users
  # GET /calcentral_users.json
  def index
    @calcentral_users = CalcentralUser.all

    render json: @calcentral_users
  end

  # GET /calcentral_users/1
  # GET /calcentral_users/1.json
  def show
    @calcentral_user = CalcentralUser.find(params[:id])

    render json: @calcentral_user
  end

  # GET /calcentral_users/new
  # GET /calcentral_users/new.json
  def new
    @calcentral_user = CalcentralUser.new

    render json: @calcentral_user
  end

  # POST /calcentral_users
  # POST /calcentral_users.json
  def create
    @calcentral_user = CalcentralUser.new(params[:calcentral_user])

    if @calcentral_user.save
      render json: @calcentral_user, status: :created, location: @calcentral_user
    else
      render json: @calcentral_user.errors, status: :unprocessable_entity
    end
  end

  # PATCH/PUT /calcentral_users/1
  # PATCH/PUT /calcentral_users/1.json
  def update
    @calcentral_user = CalcentralUser.find(params[:id])

    if @calcentral_user.update_attributes(params[:calcentral_user])
      head :no_content
    else
      render json: @calcentral_user.errors, status: :unprocessable_entity
    end
  end

  # DELETE /calcentral_users/1
  # DELETE /calcentral_users/1.json
  def destroy
    @calcentral_user = CalcentralUser.find(params[:id])
    @calcentral_user.destroy

    head :no_content
  end
end
