def _annotate_with_past_uses(cls, queryset, user):
        if queryset.model == conditions.DiscountForCategory:
            matches = (
                Q(category=F('discount__discountitem__product__category'))
            )
        elif queryset.model == conditions.DiscountForProduct:
            matches = (
                Q(product=F('discount__discountitem__product'))
            )
        in_carts = (
            Q(discount__discountitem__cart__user=user) &
            Q(discount__discountitem__cart__status=commerce.Cart.STATUS_PAID)
        )
        past_use_quantity = When(
            in_carts & matches,
            then="discount__discountitem__quantity",
        )
        past_use_quantity_or_zero = Case(
            past_use_quantity,
            default=Value(0),
        )
        queryset = queryset.annotate(
            past_use_count=Sum(past_use_quantity_or_zero)
        )
        return queryset