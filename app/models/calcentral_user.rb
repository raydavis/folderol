class CalcentralUser < ActiveRecord::Base
  attr_accessible :firstLogin, :link, :preferredName, :uid
end
