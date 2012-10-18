class CreateCalcentralUsers < ActiveRecord::Migration
  def change
    create_table :calcentral_users do |t|
      t.string :uid
      t.string :preferredName
      t.string :link
      t.string :firstLogin

      t.timestamps
    end
  end
end
