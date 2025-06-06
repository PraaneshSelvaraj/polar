"""Change cascade constraint on ProductPrice foreign keys

Revision ID: 26bf49ca1f06
Revises: da0ad0290fb4
Create Date: 2025-03-28 13:57:58.703635

"""

import sqlalchemy as sa
from alembic import op

# Polar Custom Imports

# revision identifiers, used by Alembic.
revision = "26bf49ca1f06"
down_revision = "da0ad0290fb4"
branch_labels: tuple[str] | None = None
depends_on: tuple[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        "billing_entry_product_price_id_fkey", "billing_entry", type_="foreignkey"
    )
    op.create_foreign_key(
        op.f("billing_entry_product_price_id_fkey"),
        "billing_entry",
        "product_prices",
        ["product_price_id"],
        ["id"],
        ondelete="restrict",
    )
    op.drop_constraint(
        "order_items_product_price_id_fkey", "order_items", type_="foreignkey"
    )
    op.create_foreign_key(
        op.f("order_items_product_price_id_fkey"),
        "order_items",
        "product_prices",
        ["product_price_id"],
        ["id"],
        ondelete="restrict",
    )
    op.drop_constraint(
        "subscription_product_prices_product_price_id_fkey",
        "subscription_product_prices",
        type_="foreignkey",
    )
    op.create_foreign_key(
        op.f("subscription_product_prices_product_price_id_fkey"),
        "subscription_product_prices",
        "product_prices",
        ["product_price_id"],
        ["id"],
        ondelete="restrict",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        op.f("subscription_product_prices_product_price_id_fkey"),
        "subscription_product_prices",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "subscription_product_prices_product_price_id_fkey",
        "subscription_product_prices",
        "product_prices",
        ["product_price_id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        op.f("order_items_product_price_id_fkey"), "order_items", type_="foreignkey"
    )
    op.create_foreign_key(
        "order_items_product_price_id_fkey",
        "order_items",
        "product_prices",
        ["product_price_id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        op.f("billing_entry_product_price_id_fkey"), "billing_entry", type_="foreignkey"
    )
    op.create_foreign_key(
        "billing_entry_product_price_id_fkey",
        "billing_entry",
        "product_prices",
        ["product_price_id"],
        ["id"],
        ondelete="CASCADE",
    )
    # ### end Alembic commands ###
