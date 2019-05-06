def hit1(st, ex, hiter):
    div_sex = 1
    div_subject = 1
    if self.sex == student.sex:
        div_sex = 0
    if self.subject == student.subject:
        div_subject = 0
    if hiter == 'student':
        hit = 5(div_subject + div_sex) + max(1, st.intellect - ex.knowlege) * (st.luck + max_stat) // max_stat + max(0,
                                                                                                                     st.oratory - ex.alcohol_liking) * ex.friendliness // max_stat
    else:
        hit = 2(div_subject + div_sex) + max(0, ex.knowlege - st.intellect) * (max_stat - st.luck) // max_stat + max(0,
                                                                                                                     ex.alcohol_liking - st.oratory) * ex.friendliness // max_stat
    return hit


def hit2(st, ex, hiter):
    div_sex = 1
    div_subject = 1
    if self.sex == student.sex:
        div_sex = 0
    if self.subject == student.subject:
        div_subject = 0
    if hiter == 'student':
        hit = max(0,
                  div_subject + div_sex + st.intellect - ex.knowlege + st.luck + st.oratory - ex.alcohol_liking + ex.friendliness)
    else:
        hit = max(0, div_subject + div_sex + ex.knowlege - st.intellect - st.luck +
                  ex.alcohol_liking - st.oratory + ex.friendliness)
        return hit
