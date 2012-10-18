require 'test_helper'

class CalcentralUsersControllerTest < ActionController::TestCase
  setup do
    @calcentral_user = calcentral_users(:one)
  end

  test "should get index" do
    get :index
    assert_response :success
    assert_not_nil assigns(:calcentral_users)
  end

  test "should get new" do
    get :new
    assert_response :success
  end

  test "should create calcentral_user" do
    assert_difference('CalcentralUser.count') do
      post :create, calcentral_user: { :firstLogin => @calcentral_user.firstLogin, :link => @calcentral_user.link, :preferredName => @calcentral_user.preferredName, :uid => @calcentral_user.uid }
    end

    assert_response 201
  end

  test "should show calcentral_user" do
    get :show, id: @calcentral_user
    assert_response :success
  end

  test "should update calcentral_user" do
    put :update, id: @calcentral_user, calcentral_user: { :firstLogin => @calcentral_user.firstLogin, :link => @calcentral_user.link, :preferredName => @calcentral_user.preferredName, :uid => @calcentral_user.uid }
    assert_response 204
  end

  test "should destroy calcentral_user" do
    assert_difference('CalcentralUser.count', -1) do
      delete :destroy, id: @calcentral_user
    end

    assert_response 204
  end
end
